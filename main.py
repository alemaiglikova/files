import os
for root, dirs, files in os.walk(r'C:\Users\Алема милашка\PycharmProjects\pythonProject3'):
    for file in files:
         if(os.path.isfile("for_delete.txt")):
           os.remove("for_delete.txt")
           print("File Deleted successfully")
         else:
           continue

