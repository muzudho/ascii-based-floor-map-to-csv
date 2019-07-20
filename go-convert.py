#
# Note.
#
# Root directory: Visual studio code workspace root.
#
input_file_name = "./ascii-floor-map-to-csv/data/block-map.txt"
output_file_name = "./ascii-floor-map-to-csv/auto-generated/floor-map.csv"

try:
    in_file = open(input_file_name)

    try:
        out_file = open(output_file_name, 'w', encoding='utf-8')

        out_file.write("X,Y,BLOCK\n")

        lines = in_file.readlines()
        for y, line in enumerate(lines):
            for x, block in enumerate(line):
                if block != '\n':
                    out_file.write("{},{},{}\n".format(x, y, block))
    except Exception as e:
        print(e)
    finally:
        out_file.close()

except Exception as e:
    print(e)
finally:
    in_file.close()

print("Info    : Finished.")
