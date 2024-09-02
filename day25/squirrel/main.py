import pandas

data = pandas.read_csv("squirrel_count.csv")
squirrel_by_color = data['Primary Fur Color'].value_counts()

new_frame = pandas.DataFrame(squirrel_by_color) 
new_frame.to_csv("las_cueres_del_esquilitos.csv")
print(new_frame)
