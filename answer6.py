def table(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    data = [line.strip().split(',') for line in lines]

    col_widths = []
    for i in range(len(data[0])):
        max_length = max(len(row[i]) for row in data)
        col_widths.append(max_length)

    border = '+'
    for width in col_widths:
        border += '-' * width + '+'

    print(border)
    for i, row in enumerate(data):
        row_str = '|'
        for j in range(len(row)):
            cell_value = row[j]
            column_width = col_widths[j]
            row_str += cell_value.ljust(column_width) + '|'
        print(row_str)

        if i == 0:
            print(border)
    print(border)

table("/home/priyanshi/Documents/data.csv")
