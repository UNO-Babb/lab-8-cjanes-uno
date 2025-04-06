#ProcessData.py
#Name: Colton Janes
#Date: 04/05/2025
#Assignment: Lab 8

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  outFile.write("Last Name,First Name,User ID,Major-Year\n") #Creating a header row for the .csv file

  #Process each line of the input file and output to the CSV file
  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    idNum = data[3]
    major = data[6]
    year = data[5]
    
    student_id = makeUserID(first, last, idNum)
    major_year = majorYear(major, year)
    output = last + "," + first + "," + student_id + "," + major_year + "\n"
    outFile.write(output)

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeUserID(first, last, idNum):
  """Function to create a User ID based on the first letter of the first name, the full last name, and the last three numbers of their student ID number."""
  first = first.lower() #Choosing to use lowercase is my personal preference and aligns to how UNO's appears generally.
  last = last.lower()

  idLen = len(idNum)
  
  while len(last) < 5:
    last = last + "x"
  
  id = first[0] + last + idNum[idLen - 3: ]
  
  return id

def majorYear(major, year):
  """Function to create a Major-Year value based on the first three letters of the student's major and an abbreviated two-letter representation of their year in school. Both major and year values are separated by a hyphen."""
  #For this specific use, I chose to consolidate the major and year "problems" into one.
  #For wider application/use and using in a variety of programs, probably better practice to separate them out.
  major = major.upper() #I assume it's cleaner to have the output 3 characters be capitalized.
  year = year.lower() #I assume this to be the correct/preferred decision to avoid future sources using all caps or a variance.

  while len(major) < 3: #Pretty sure there aren't any majors that are less than 3 characters, so this might be unnecessary.
    major = major + "X"

  year_abbr = {"freshman":"FR", "sophomore":"SO", "junior":"JR", "senior":"SR"} #Creating a dictionary based on pair values.
  
  if year in year_abbr: #Checks that the value for year exists in the dictionary created above.
    short_year = year_abbr[year]
  else:
    short_year = "NA" #I'm not seeing any missing year values in this set, so this might be unnecessary.

  majorYear = major[ :3] + "-" + short_year

  return majorYear

if __name__ == '__main__':
  main()
