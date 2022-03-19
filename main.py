# Main Code for the Problem of Moving Zeros to the End of an Arbitrary Array of Numbers!
# Written by Shahab Bahrami
# March 2022

def MovingZeros(arr):
    if len(arr)==0:
        return arr
    else:
        locPointer = 0
        temp = 0
        for i in range(len(arr)):
            if arr[i]!=0:
                temp = arr[locPointer]
                arr[locPointer] = arr[i]
                arr[i] = temp
                locPointer +=1
        return arr
