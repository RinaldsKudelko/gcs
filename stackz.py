
allowed_size = 3        #Stack height
size = 0
container_count = 13    #Container Count
container_columns = 0
symbol = "M"            #symbol for visualization

#Calculate columns and remeinder
while container_count > 0:
    size += 1
    if(size == allowed_size):
        container_columns += 1
        size = 0
    container_count -= 1

#Visualize
for i in range(allowed_size):
    if(size > 0):
        print(symbol * container_columns + symbol)
        size -= 1
    else:
        print(symbol * container_columns)
