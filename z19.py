import csv


def write_file():
    with open('z19exc.csv', encoding='utf8') as f:
        reader = csv.reader(f)
        # for row in reader:
        #     print(row)
        print(list(reader))


# write_file()


# with open('z19exc.csv', encoding='utf8') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row['location'])


users = [
    ['Tom', 28],
    ['Alice', 23],
    ['Bob', 34],
]

with open('file.csv', 'w', encoding='utf8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(users)

with open('file.csv', 'a', encoding='utf8') as file:
    user = ['Sam', 31]
    writer = csv.writer(file)
    writer.writerow(user)


data = [
    ['hostname', 'vendor', 'model', 'location'],
    ['sw1', 'Cisco', '3750', 'Best str'],
    ['sw2', 'Cisco', '3850', 'Better str'],
    ['sw3', 'Cisco', '3650', 'Better str'],
    ['sw4', 'Cisco', '3650', 'Best str'],
]

with open('new_file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)


data = {
    'hostname': 'sw1',
    'location': 'London',
    'model': '3750',
    'vendor': 'Cisco',
}, {
    'hostname': 'sw2',
    'location': 'Liverpool',
    'model': '3850',
    'vendor': 'Cisco',
}, {
    'hostname': 'sw3',
    'location': 'London',
    'model': '3650',
    'vendor': 'Cisco',
}, {
    'hostname': 'sw4',
    'location': 'Liverpool',
    'model': '3650',
    'vendor': 'Cisco',
}
with open('file_dictwriter.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=(data[0].keys()))
    writer.writeheader()
    for d in data:
        writer.writerow(d)

with open('file.csv') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        print(row)
