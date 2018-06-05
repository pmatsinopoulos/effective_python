def print_lines(file_handle):
    for line in file_handle:
        yield line.strip()


with open('test-data/file-with-lines.txt', 'r') as f:
    generator = print_lines(f)
    for line in generator:
        print(line)
