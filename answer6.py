def read_csv(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip().split(',') for line in lines]

def width(data):
    col = len(data[0])
    col_width = [0] * col

    for col in range(col):
        maxi = 0
        for row in data:
            length = len(row[col])
            if length > maxi:
                maxi = length
        col_width[col] = maxi
    return col_width


def table(data):
    col_widths = width(data)
    border = '+' + '+'.join('-' * (width) for width in col_widths) + '+'
    
    print(border)
    for i, row in enumerate(data):
        
        row_str = '|'

        for j in range(len(row)):
    
            cell_value = row[j]
            
            column_width = col_widths[j]
            
            formatted_cell = f'{cell_value:<{column_width}}'
            
            row_str += formatted_cell + '|'

        print(row_str)
    
        if i == 0:
            print(border)

csv_file_path = "data.csv" 
data = read_csv("/home/priyanshi/Documents/data.csv")
table(data)
