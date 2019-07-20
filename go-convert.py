#
# Note.
#
# Root directory: Visual studio code workspace root.
#
input_file_name = "./ascii-floor-map-to-csv/data/floor-map.txt"
output_file_name = "./ascii-floor-map-to-csv/auto-generated/floor-map.csv"

try:
    in_file = open(input_file_name)

    try:
        out_file = open(output_file_name, 'w', encoding='utf-8')

        out_file.write("X,Y,CHAR\n")

        lines = in_file.readlines()
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char != '\n':
                    out_file.write("{},{},{}\n".format(x, y, char))
    except Exception as e:
        print(e)
    finally:
        out_file.close()

except Exception as e:
    print(e)
finally:
    in_file.close()

print("Info    : Finished.")
