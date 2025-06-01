import os
import sys

def main():
    if len(sys.argv) != 4 or sys.argv[2] != "--text":
        sys.exit(1)
    
    folder_path = sys.argv[1]
    search_text = sys.argv[3]
    
    try:
        log_files = [f for f in os.listdir(folder_path) 
                    if os.path.isfile(os.path.join(folder_path, f)) 
                    and f.endswith('.log')]
    except PermissionError: 
        print(f"Не нашли файл '{folder_path}'")
        sys.exit(1)


    for log_file in log_files:
        file_path = os.path.join(folder_path, log_file)
        
        try:
            with open(file_path, 'r') as file:
                line_number = 0
                
                for line in file:
                    line_number += 1
                    
                    if search_text in line:
                        words = line.split()
                        try:
                            index = words.index(search_text)
                            start = max(0, index - 5)
                            end = min(len(words), index + 6)
                            context = ' '.join(words[start:end])
                        except ValueError:
                            context = line.strip()
                         
                        print(f"Файл: {log_file}, Строка: {line_number}")
                        
        except UnicodeDecodeError:
            print(f"Ошибка: Файл '{log_file}' не является текстовым файлом в кодировке UTF-8")
        except PermissionError:
            print(f"Ошибка: Нет доступа к файлу '{log_file}'")

if __name__ == "__main__":
    main()