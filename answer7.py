def get_sizes():
    return ["nano", "micro", "small", "medium", "large", "xlarge", "2xlarge", "4xlarge", "8xlarge", "16xlarge", "32xlarge"]

def recommend(ec2_type, cpu):
    family, size = ec2_type.split('.')
    sizes = get_sizes()
    index = sizes.index(size) if size in sizes else -1
    
    if cpu < 20:
        status = "Underutilized"
        new_size = sizes[index - 1] if index > 0 else size
    elif 20 <= cpu <= 80:
        status = "Optimized"
        new_size = size
    else:
        status = "Overutilized"
        new_size = sizes[index + 1] if index < len(sizes) - 1 else size
    
    new_ec2 = family + '.' + new_size
    return status, new_ec2

def width(data):
    col_widths = []
    for i in range(len(data[0])):
        max_length = max(len(str(row[i])) for row in data)
        col_widths.append(max_length + 2)
    return col_widths

def table(data):
    col_widths = width(data)
    border = '+'
    for w in col_widths:
        border += '-' * w + '+'
    
    print(border)
    for i, row in enumerate(data):
        row_str = '|'

        for j in range(len(row)):
            cell = row[j]
            col_width = col_widths[j]
            row_str += cell.ljust(col_width) + '|'

        print(row_str)

        if i == 0:
            print(border)
    print(border)

ec2 = "t2.large"
cpu = 90

status, rec_ec2 = recommend(ec2, cpu)
rows = [
    ["No.", "Current EC2", "CPU", "Status", "Recommended EC2"],
    ["1", ec2, str(cpu) + "%", status, rec_ec2]
]
table(rows)
