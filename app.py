import time

def count_to_10():
    print("Starting the couting application ...")
  
    for i in range(1, 11):      
        print(i)
        time.sleep(1)

if __name__ == "__main__":
    count_to_10()
