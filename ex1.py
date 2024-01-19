import csv
from io import TextIOWrapper
from zipfile import ZipFile

# opens file for oscars table.
# CHANGE!

Films = open("films.csv", 'w')
films_writer = csv.writer(Films, delimiter=",", quoting=csv.QUOTE_NONE)
was_awarded = open("was_awarded.csv", 'w')
was_awarded_writer = csv.writer(was_awarded, delimiter=",", quoting=csv.QUOTE_NONE)
oscar_cermony = open("oscar_cermony.csv", 'w')
oscar_cermony_writer = csv.writer(oscar_cermony, delimiter=",", quoting=csv.QUOTE_NONE)



# process_file goes over all rows in original csv file, and sends each row to process_row()
# DO NOT CHANGE!!!
def process_file():
    with ZipFile('archive.zip') as zf:
        with zf.open('oscars_df.csv', 'r') as infile:
            reader = csv.reader(TextIOWrapper(infile, 'utf-8'))
            for row in reader:
                # remove some of the columns
                chosen_indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14, 15, 16, 29]
                row = [row[index] for index in chosen_indices]

                # change "," into && in list values
                lists_values_indices = [7, 11, 12, 13]
                for list_value_index in lists_values_indices:
                    row[list_value_index] = row[list_value_index].replace(',', '&&')

                # pre-process : remove all quotation marks from input and turns NA into null value ''.
                row = [v.replace(',', '') for v in row]
                row = [v.replace("'", '') for v in row]
                row = [v.replace('"', '') for v in row]
                row = [v if v != 'NA' else "" for v in row]

                # In the first years of oscars in the database they used "/" for example 1927/28, so we will change these.
                row[2] = row[2].split("/")[0]

                # In 1962 two movies were written as winners, then we change one of them to nominee.
                if row[4] == "Winner" and row[2] == "1962" and row[14] == "8d5317bd-df12-4f24-b34d-e5047ef4665e":
                    row[4] = "Nominee"

                # In 2020 Nomadland won and marked as nominee by mistake.
                if row[2] == "2020" and row[1] == "Nomadland":
                    row[4] = "Winner"

                process_row(row)

    # flush and close the file. close all of your files.
    Films.close()
    was_awarded.close()
    oscar_cermony.close()


# return a list of all the inner values in the given list_value.
# you should use this to handle value in the original table which
# contains an inner list of values.
# DO NOT CHANGE!!!
def split_list_value(list_value):
    return list_value.split("&&")

# process_row should splits row into the different csv table files
# CHANGE!!!
def process_row(row):
    something = [row[0], row[1], row[3], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12],
                 row[13], row[14]]
    films_writer.writerow(something)
    was_awarded_writer.writerow([row[2], row[14], row[4]])
    oscar_cermony_writer.writerow([row[2]])


# return the list of all tables
# CHANGE!!!
def get_names():
    return ["Films", "was_awarded", "oscar_cermony"]

if __name__ == "__main__":
    process_file()

