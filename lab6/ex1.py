class Matri:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def bubble_sort_row(row):
        n = len(row)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if row[j] > row[j + 1]:
                    row[j], row[j + 1] = row[j + 1], row[j]
        return row
    
    def sort_rows(self):
        for row in self.data:
            self.bubble_sort_row(row)

    @staticmethod
    def calculate_sums_below_anti_diag(sorted_matrix):
        n = len(sorted_matrix)
        sums = []
        for col in range(n):
            elements = []
            for row in range(n):
                if row + col > n - 1:
                    elements.append(sorted_matrix[row][col])
            sums.append(elements)
        sums_sum = [sum(col_elements) for col_elements in sums]
        return sums, sums_sum

    @staticmethod
    def geometric_mean(values):
        result = []
        for value_list in values:
            if value_list:
                product = 1
                for value in value_list:
                    if value <= 0:
                        result.append(0)
                        break
                    product *= value
                else:
                    mean = product ** (1 / len(value_list))
                    result.append(round(mean, 2))
            else:
                result.append(0)
        return result

    def __str__(self):
        return "\n".join(str(row) for row in self.data)


matrix = Matri([
    [87, 98, 57, 29, 95],
    [-8, 59, -2, 9, -11],
    [6, 10, 20, 59, -23],
    [12, 13, 51, 46, -7],
    [-2, 87, 69, 90, -3]
])

print("Оригінальна матриця:")
print(matrix, "\n")

matrix.sort_rows()
print("Сортована матриця:")
print(matrix, "\n")

sorted_matrix_elements, sorted_matrix_sums = Matri.calculate_sums_below_anti_diag(matrix.data)

print("Сума елементів під побічною діагоналлю для кожного стовпця:")
print(sorted_matrix_sums, "\n")

product = Matri.geometric_mean(sorted_matrix_elements)
print("Середнє геометричне для кожного стовпця:")
print(product)
