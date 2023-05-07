with  open('1.txt', encoding='utf-8') as file1:
    result1 = file1.readlines()
initial_values1 = ['1.txt', f'\n', str(len(result1)), f'\n']
with  open('2.txt', encoding='utf-8') as file2:
    result2 = file2.readlines()
initial_values2 = ['2.txt', f'\n', str(len(result2)), f'\n']
with  open('3.txt', encoding='utf-8') as file3:
    result3 = file3.readlines()
initial_values3 = ['3.txt', f'\n', str(len(result3)), f'\n']

result1full = initial_values1 + result1
result2full = initial_values2 + result2
result3full = initial_values3 + result3
list_files = [result1full, result2full, result3full]
list_files.sort(key=len)

with open('4.txt', 'w', encoding='utf-8') as file4:
    for file in list_files:
        file4.writelines(file)
        file4.write(f'\n')
