import csv

def baca_pesanan():
    pesanan = []

    with open("data/pesanan.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            pesanan.append(row)

    return pesanan

class DynamicArray:
    def __init__(self, kapasitas_awal=10):
        self.data = [None] * kapasitas_awal
        self.size = 0
        self.capacity = kapasitas_awal

    def tambah(self, pesanan):
        # Kalau array sudah penuh, kapasitas digandakan
        if self.size == self.capacity:
            self.capacity *= 2

            data_baru = [None] * self.capacity

            for i in range(self.size):
                data_baru[i] = self.data[i]

            self.data = data_baru

        self.data[self.size] = pesanan
        self.size += 1

    def lihat_semua(self):
        hasil = []

        for i in range(self.size):
            hasil.append(self.data[i])

        return hasil

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def tambah_belakang(self, pesanan):
        node_baru = Node(pesanan)

        if self.head is None:
            self.head = node_baru
            self.tail = node_baru
        else:
            self.tail.next = node_baru
            self.tail = node_baru

        self.size += 1

    def lihat_semua(self):
        hasil = []

        current = self.head

        while current is not None:
            hasil.append(current.value)
            current = current.next

        return hasil

data = baca_pesanan()

# Dynamic Array
array_pesanan = DynamicArray()

for pesanan in data:
    array_pesanan.tambah(pesanan)

# Linked List
linked_pesanan = LinkedList()

for pesanan in data:
    linked_pesanan.tambah_belakang(pesanan)


print("=== DYNAMIC ARRAY ===")
print("Jumlah pesanan:", array_pesanan.size)
print("Kapasitas array:", array_pesanan.capacity)
print("Pesanan pertama:")
print(array_pesanan.data[0])

print()

print("=== LINKED LIST ===")
print("Jumlah pesanan:", linked_pesanan.size)
print("Pesanan pertama:")
print(linked_pesanan.head.value)