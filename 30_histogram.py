import matplotlib.pyplot as plt

data=list(map(int,input("Enter heights of student:").split()))

plt.hist(data,bins=5,edgecolor="black")
plt.title("Heights of students in Class")
plt.show()