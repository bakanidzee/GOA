
#კოდი გამოიტანს ერორს, რადგან Python-ში int (მაგ. a = 5) და str (მაგ. b = "10") ტიპების პირდაპირი კომბინაცია არ არის შესაძლებელი. a არის მთელი რიცხვი, ხოლო b არის სტრინგი, ამიტომ მათ დაჯამებისას Python ვერ დაპრინტავს.

# პირველი ხერხი

a = 5
b = "10"
result = a + int(b)
print("Result:", result)

# მეორე ხერხი

a = 5
b = "10"
result = str(a) + b
print("Result:", result)
