import csv

with open('z19exc.csv', 'r', encoding='utf8') as f:
    reader = csv.reader(f)
    for r in reader:
        if r:
            print(r)

with open('z19exc.csv', 'r', encoding='utf8') as f2:
    reader = csv.reader(f2)
    print(list(reader))

with open('z19exc.csv', 'r', encoding='utf8') as f3:
    reader = csv.DictReader(f3)
    for r in reader:
        print(r)


a = {
    'name': 'Alice',
    'surname': 'Brown',
    'age': '32',
    'location': 'London',
}, {
    'name': 'Timur',
    'surname': 'Leonov',
    'age': '19',
    'location': 'Mocsow',
}, {
    'name': 'Robert',
    'surname': 'Paulson',
    'age': '48',
    'location': 'San-Francisco',
}
b = ['name', 'surname', 'age', 'location']
with open('z19z2.csv', 'w', encoding='utf8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=b)
    writer.writeheader()
    writer.writerows(a)

