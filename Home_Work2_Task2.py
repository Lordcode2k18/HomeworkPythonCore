while True:
    number=int(input("Enter four-digit number\n"))
    if number>=1000 and number<=9999:
        break

#spr_list_of_numbers=number.split()
figure1=number//1000 
figure2=(number//100)%10
figure3=(number%100)//10
figure4=number%10
list_of_figure=[figure1, figure2, figure3, figure4]
list_of_figure.sort()
print(figure1*figure2*figure3*figure4)
print(str(figure4)+str(figure3)+str(figure2)+str(figure1))
print(list_of_figure)