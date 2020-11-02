# Binary Search Algorithm
# Author: Obaid Nadeem
# Python 3.8


def main():

    def searchAlgo(arr,min_val,max_val,val_to_find):

        if max_val >= min_val:
            mid = int(min_val + ((max_val - min_val) // 2))

            if val_to_find == arr[mid]:
                return mid            
            elif val_to_find < arr[mid] :
                return searchAlgo(arr, min_val , mid - 1 , val_to_find)
            elif val_to_find > arr[mid] :
                return searchAlgo(arr , mid + 1 , max_val  , val_to_find)
        else:
            return -1

    arr = []
    arrayLength = int(input("How may numbers you want to store? : "))


    for i in range(arrayLength):
        number = int(input("Enter the value: "))
        arr.append(number)



    arr.sort()
    val_to_find = int(input("Enter the value to be found: ")) 

    result = searchAlgo(arr,0,len(arr)-1,val_to_find)

    if result != -1:
        print("The index of the number is {}".format(result))
    else:
        print("Number is not present in the array ! ")

main()