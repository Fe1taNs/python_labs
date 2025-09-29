name = input("ФИО: ")
f_name = ' '.join(name.strip().split())
name_parts = f_name.split()

i_list = [part[0].upper() for part in name_parts]

i = ''.join(i_list)

print(f"Инициалы: {i}.")
print(f"Длина (символов): {len(f_name)}")