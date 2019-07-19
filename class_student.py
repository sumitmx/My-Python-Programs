# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 16:44:41 2019

@author: PANKAJ
"""


class Student:
    # def __init__(self):
    #     self.rollno = 1
    #     self.name = ""
    #     self.location = ""
    #     self.s1marks = 1

    def filldetails(self):
        self.rollno = int(input("Enter the rollno: \n"))
        self.name = input("Enter the name: \n")
        self.location = input("Enter the location: \n")
        self.s1marks = int(input("Enter the s1marks: "))

    def introduceyourself(self):
        print(self.rollno , self.name, self.location, self.s1marks)

    @classmethod
    def search(cls):
        search = int(input('Enter the roll no. to search: \n'))

        for i in range(len(stu_list)):
            if stu_list[i].rollno == search:
                stu_list[i].introduceyourself()
                break
        if len(stu_list)!=0 and stu_list[i].rollno != search:       #this is to check if list is not empty and also the rollno. is not found
            print('rollno does not exists')
        elif stu_list[i].rollno == search:
            pass
        else:
            print('NA')


class Courses:
    def __init__(self):
        self.cid = -1
        self.cname = ""
        self.cduration = -1

stu_list=[]

choice = -1
while choice != 4:
    print("\n\n***MENU****")
    print("1. Add Student: ")
    print("2. Display All Student: ")
    print("3. Search based on rollno: ")
    print("4. Exit")

    choice = int(input("Enter the choice: "))
    if choice == 1:
        print("Add Student")
        s = Student()
        stu_list.append(s)

        stu_list[-1].filldetails()
    elif choice == 2:
        print('Display all Student ')

        for obj in stu_list:
            obj.introduceyourself()
    elif choice == 3:
        Student.search()                    # Calling the class method using class name
    elif choice == 4:
        print("Thank you for using my software ")
    else:
        print("Please enter the valid option.")








