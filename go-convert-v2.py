#
# Note.
#
# Root directory: Visual studio code workspace root.
#
block_input_file = "./ascii-floor-map-to-csv/data/floor-map.txt"
table_input_file = "./ascii-floor-map-to-csv/data/table-number-map.txt"
output_file_name = "./ascii-floor-map-to-csv/auto-generated/floor-map.csv"

try:
    bl_file = open(block_input_file)
    try:
        ta_file = open(table_input_file)

        try:
            out_file = open(output_file_name, 'w', encoding='utf-8')

            out_file.write("ID, X,Y,CHAR\n")
            id_column = []
            x_column = []
            y_column = []
            block_column = []

            bl_lines = bl_file.readlines()
            for y, line in enumerate(bl_lines):
                for x, char in enumerate(line):
                    if char != '\n':
                        x_column.append(x)
                        y_column.append(y)
                        block_column.append(char)

            ta_lines = ta_file.readlines()
            for row in ta_lines:
                cols = row.split(",")
                for x, number_text in enumerate(cols):
                    num = int(number_text)
                    if num != 0:
                        id_column.append(num)

            for i, id in enumerate(id_column):
                out_file.write("{},{},{},{}\n".format(
                    id, x_column[i], y_column[i], block_column[i]))

        except Exception as e:
            print(e)
        finally:
            out_file.close()

    except Exception as e:
        print(e)
    finally:
        ta_file.close()
except Exception as e:
    print(e)
finally:
    bl_file.close()

print("Info    : Finished.")
