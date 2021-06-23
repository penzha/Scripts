import matplotlib.pyplot as plt
import numpy as np

dict = {}

file = open('hugepages_usage.log', 'r')
try:
    log_lines = file.readlines()
    #print(type(log_lines), log_lines)
    for line in log_lines:
        #print(type(line), line)
        dict[line.split("\t")[0]] = line.split("\t")[1]
finally:
    file.close()

#print (dict)

#plt.plot(["Tue Jun 22 17:23:07 2021", "Tue Jun 22 17:23:12 2021", "Tue Jun 22 17:23:17 2021"], [6784,6912,7680])

plt.plot(dict.keys(), dict.values())
plt.xticks(rotation=90)

plt.xlabel('Date')
plt.ylabel('HugePages')
plt.title('HugePages Usage (MB)')
plt.grid(True)
plt.legend()

plt.show()


#np.random.seed(1999999)
#data = np.random.randn(2, 100)

#plt.plot(df['Mes'], df['data science'], label='data science') #The parameter label is to indicate the legend. This doesn't mean that it will be shown, we'll have to use another command that I'll explain later.

#plt.plot(df ['Mes']，df ['data science']，label ='data science')
#plt.plot(df ['Mes']，df ['machine learning']，label ='machine learning ')
#plt.plot(df ['Mes']，df ['deep learning']，label ='deep learning')

#fig, axs = plt.subplots(2, 2, figsize=(5, 5))
#axs[0, 0].hist(data[0])
#axs[1, 0].scatter(data[0], data[1])
#axs[0, 1].plot(data[0], data[1])
#axs[1, 1].hist2d(data[0], data[1])