import os
import yaml

def remove_duplicate_templates(folder_path, file_extensions):
    ids = set()
    names = set()
    duplicates = set()      # ✅ Dùng set để tránh trùng
    name_error = set()

    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_extension = os.path.splitext(filename)[1].lower()
            if file_extension in file_extensions:
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                        data = yaml.safe_load(f)
                except yaml.YAMLError as e:
                    print(f'[YAML ERROR] {file_path}: {e}')
                    continue
                except Exception as e:
                    print(f'[READ ERROR] {file_path}: {e}')
                    continue

                if isinstance(data, dict) and 'info' in data:
                    info = data['info']
                    name_value = info.get('name')
                    id_value = data.get('id')

                    if id_value and id_value in ids:
                        duplicates.add(file_path)
                        print(f'[DUPLICATE ID] {file_path}')
                    else:
                        ids.add(id_value)

                    if name_value and '\n' in name_value:
                        name_error.add(file_path)
                        print(f'[NAME ERROR] Name contains newline: {file_path}')

                    if name_value and name_value in names:
                        duplicates.add(file_path)
                        print(f'[DUPLICATE NAME] {file_path}')
                    else:
                        names.add(name_value)

    # Ghi log & xóa file trùng lặp
    with open('duplicate_files.txt', 'w', encoding='utf-8') as f:
        for duplicate in sorted(duplicates):
            if os.path.exists(duplicate):
                try:
                    os.remove(duplicate)
                    f.write(f"{duplicate}\n")
                    print(f'[REMOVED DUPLICATE] {duplicate}')
                except Exception as e:
                    print(f'[ERROR REMOVING] {duplicate}: {e}')

    # Xóa file chứa tên bị lỗi
    for file in sorted(name_error):
        if os.path.exists(file):
            try:
                os.remove(file)
                print(f'[REMOVED NAME ERROR] {file}')
            except Exception as e:
                print(f'[ERROR REMOVING NAME ERROR] {file}: {e}')

    print(f"\n✅ Removed {len(duplicates)} duplicate files and {len(name_error)} files with name errors.")

if __name__ == '__main__':
    folder_path = r'D:\bug-bounty\nuclei-templates-cutomer\community-templates'
    file_extensions = ('.yaml', '.yml')

    remove_duplicate_templates(folder_path, file_extensions)
