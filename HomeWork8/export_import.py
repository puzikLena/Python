
def get_file_name() -> str:
    return input('Введите имя файла: ')

def get_batch_data(name_file: str) -> list: # Импорт данных
    lst = []
    with open('phonebook_8_sem.csv', 'r', encoding='utf-8') as file:
        for line in file:
            lst.append(list(line.strip().split('#')))
        return lst

def record_data(name_file, data): # Экспорт данных
    with open ('phonebook_8_Sem_new.csv', 'w', encoding='utf-8') as file:
        for el in data:
            file.write(f'{el[0]};{el[1]};{el[2]};{el[3]}\n')