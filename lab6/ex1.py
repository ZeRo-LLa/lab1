class Matri:
    def __init__(self,data):
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
    def calculate_sums_below_diag(sorted_matrix):
        n = len(sorted_matrix)
        sums = [0] * n
        for col in range(n):
            for row in range(n):
                if row + col > n - 1:
                    sums[col] += sorted_matrix[row][col]
        return sums

    @staticmethod
    def geometric_mean(values):
        positive_values = [val for val in values if val > 0]
        if len(positive_values) > 0:
            product = 1
            for val in positive_values:
                product *= val
            return product ** (1 / len(positive_values))
        return 0
    
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
print(matrix, "\n" ) 

matrix.sort_rows()
print("Сортована матриця:")
print(matrix, "\n")

sorted_matrix = Matri.calculate_sums_below_diag(matrix.data)
print("Середнє значення діагоналей матриці: ")
print(sorted_matrix, "\n")

product = Matri.geometric_mean(sorted_matrix)
print("Добуток середніх значень:", product)