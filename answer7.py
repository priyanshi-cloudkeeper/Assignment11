def get_instance_hierarchy():
    return ["nano", "micro", "small", "medium", "large", "xlarge", "2xlarge", "4xlarge", "8xlarge", "16xlarge", "32xlarge"]

def recommend_instance(instance_type, cpu_utilization):
    instance_family, instance_size = instance_type.split('.')
    sizes = get_instance_hierarchy()
    size_index = sizes.index(instance_size) if instance_size in sizes else -1
    
    if cpu_utilization < 20:
        status = "Underutilized"
        recommended_size = sizes[size_index - 1] if size_index > 0 else instance_size
    elif 20 <= cpu_utilization <= 80:
        status = "Optimized"
        recommended_size = instance_size  
    else:
        status = "Overutilized"
        recommended_size = sizes[size_index + 1] if size_index < len(sizes) - 1 else instance_size
    
    recommended_instance = f"{instance_family}.{recommended_size}"
    return status, recommended_instance

def print_table(data):
    col_widths = [max(len(str(row[i])) for row in data) for i in range(len(data[0]))]
    border = '+' + '+'.join('-' * (width + 2) for width in col_widths) + '+'
    print(border)
    for i, row in enumerate(data):
        row_str = '| ' + ' | '.join(f'{row[j]:<{col_widths[j]}}' for j in range(len(row))) + ' |'
        print(row_str)
        print(border if i == 0 else '')  
    print(border)


ec2_instance = "t2.large"
cpu_utilization = 90

status, recommended_ec2 = recommend_instance(ec2_instance, cpu_utilization)
data = [["Serial No.", "Current EC2", "Current CPU", "Status", "Recommended EC2"],
        ["1", ec2_instance, f"{cpu_utilization}%", status, recommended_ec2]]

print_table(data)
