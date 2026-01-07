import numpy as np
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

year = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]


width = 0.25
indices = np.arange(len(year))


population_china = [1.359, 1.397, 1.409, 1.412, 1.413, 1.414, 1.415, 1.416, 1.417, 1.418]
population_india = [1.23, 1.309, 1.324, 1.359, 1.397, 1.409, 1.412, 1.414, 1.416, 1.418]


plt.bar(indices - width/2, population_china, width=width, color='green', label='china')
plt.bar(indices + width/2, population_india, width=width, color='red', label='india')


plt.title('population comparison between india and china')
plt.xlabel('year')
plt.ylabel('population ==> in billions')
plt.xticks(indices, year, rotation=45)
plt.legend()
plt.tight_layout()


plt.show()
