# ask the user how many days in a month
# and what day of the week the month starts on
# print the month in the terminal, with one week per line
# the first row should be the days of the week: 'S M T W T F S'
print('How many days in a month?')

how_many_days = int(input())

print('What day of the week does the month start on?' \
' Enter 1 for Sunday, 2 for Monday, 3 for Tuesday ...')

what_day = int(input())

print('S  M  T  W  T  F  S')


for i in range (what_day - 1):
    print ("   ", end="")

position = what_day - 1

for day in range(1, how_many_days + 1):
    print(f"{day:2}", end=" ")
    position += 1
    if position % 7 == 0:
        print()


print()