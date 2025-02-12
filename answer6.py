def read_csv(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip().split(',') for line in lines]

def calculate_column_widths(data):
    num_columns = len(data[0])
    column_widths = [0] * num_columns

    for col in range(num_columns):
        max_width = 0
        for row in data:
            cell_length = len(row[col])
            if cell_length > max_width:
                max_width = cell_length
        column_widths[col] = max_width
    return column_widths


def print_table(data):
    col_widths = calculate_column_widths(data)
    border = '+' + '+'.join('-' * (width +2) for width in col_widths) + '+'
    
    print(border)
    for i, row in enumerate(data):
        row_str = '| ' + ' | '.join(f'{row[j]:<{col_widths[j]}}' for j in range(len(row))) + ' |'
        print(row_str)
        print(border if i == 0 else '')  
    
    print(border)

csv_file_path = "data.csv" 
data = read_csv("/home/priyanshi/Documents/data.csv")
print_table(data)
