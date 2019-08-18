from u55_die import Die
import pygal

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1,1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

print(results)

# 分析结果
frequencies = []
max_results = die_1.num_sides + die_2.num_sides
for num_side in range(2,max_results + 1):
    frequency = results.count(num_side)
    frequencies.append(frequency)

print(frequencies)

# 对结果进行可视化

hist = pygal.Bar()
hist._title = 'Results D6 100 times'
hist.x_labels = list(range(2,max_results + 1))
hist._x_title = 'Result'
hist._y_title = 'Frequency of result'

hist.add('D6',frequencies)
hist.render_to_file('pygal.svg')