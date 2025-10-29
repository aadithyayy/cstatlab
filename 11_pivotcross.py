import pandas as pd

data={
    "Student":["Rahul","Sheetal","Sonam","Mohit"],
    "Class":["CU","CS","CU","CS"],
    "Subject":["Maths","Maths","Hindi","Hindi"],
    "Marks":[94,83,76,81],
}

dframe=pd.DataFrame(data)
print("Dataframe:\n",dframe,"\n")

pvttable=pd.pivot_table(dframe,values="Marks",index="Class",columns="Subject",aggfunc="mean")
print("Pivot Table:\n",pvttable,"\n")

cross=pd.crosstab(dframe["Subject"],dframe["Marks"])
print("Cross Tab:\n",cross,"\n")