notes_list=[2000,1000,500,200,100,50,20,10,5,1]
def atm_machine():
    print("Welcome to ATM Machine")
    x=int(input("Enter the amount which you want to withdraw:"))
    notes_count=[x//2000]+[(x%2000)//1000]+[((x%2000)%1000)//500]+[(((x%2000)%1000)%500)//200]+[((((x%2000)%1000)%500)%200)//100]+[(((((x%2000)%1000)%500)%200)%100)//50]+[((((((x%2000)%1000)%500)%200)%100)%50)//20]+[(((((((x%2000)%1000)%500)%200)%100)%50)%20)//10]+[((((((((x%2000)%1000)%500)%200)%100)%50)%20)%10)//5]+[(((((((((x%2000)%1000)%500)%200)%100)%50)%20)%10)%5)//1]
    print(notes_list)
    print(notes_count)
    count=0
    for i in notes_count:
        count=count+i
    return count
if __name__ == '__main__':
    print("Minimum number of notes are:",atm_machine())
