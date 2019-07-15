#
# Note.
#
# Root directory: Visual studio code workspace root.
#
file_name = "./ascii-floor-map-to-csv/data/floor-map.txt"

try:
    file = open(file_name)
    lines = file.readlines()
    for line in lines:
        for char in line:
            print(char)
        print("[new line]")
except Exception as e:
    print(e)
finally:
    file.close()
