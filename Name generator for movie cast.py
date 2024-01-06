#Prashanth_Krishna
#Function that finds alien names from actor names by manipulating and appending lists

#import copy for deepcopy function
import copy

#define actor name lists 
actorGivenList = ['andrei','harry','yuan','sadiq','zeng']
actorFamilyList = ['stephens','venables','spield','elbahi','ergan']

#function which extracts the 2 letters from given name and 3 letters from family name
def extract_name(actorGivenList,actorFamilyList):

    #define lists for letter components of alien names
    givenhalf = [] 
    familyhalf = []
    
    #for loop that runs for every element in the given name list
    for i in (actorGivenList):
        #use append to extract letters to new list
        givenhalf.append(i[:2])

    #same process for family name list
    for i in (actorFamilyList):
        familyhalf.append(i[:3])

    return familyhalf,givenhalf

#function that creates alien names from the extracted letters and appends them to new alien name list
def alien_name(familyhalf,givenhalf):
    #define list for alien names
    alienNameList = []

    #for loop that runs for the amount of elements in the given name list,(same amount as family name list)
    for i in range (len(actorGivenList)):
        #define new strings for each group of letters from each name 
        twogiven = givenhalf[i]
        threefamily = familyhalf[i]

        #create new alien name from adding the two strings together 
        alienName = threefamily+twogiven
        #use append to add new names to the list for alien names
        alienNameList.append(alienName)

    return alienNameList

#function which finds and defines the directors given and family name
def director_name(familyhalf):

    #use deepcopy to make original copies of given and family name lists 
    director_given_name = copy.deepcopy(familyhalf)
    director_family_name = copy.deepcopy(familyhalf)

    #define two new strings to use for directors given and family name
    directorGivenName = ""
    directorFamilyName = ""

    #use del to delete the elements which are needed for the directors given and family names respectively
    #(spi,elb,erg: not needed for given name),(ste,ven: not needed for family name)
    del director_given_name [2:5]
    del director_family_name [0:2]

    #for loop that runs for the amount of elements in given name list
    for i in range (len(director_given_name)):
        #define new string for each part of given name
        given_part_name = director_given_name[i]
        #find directors name by adding the sections of his name to the new string
        directorGivenName = directorGivenName + given_part_name

    #same process for family name
    for i in range (len(director_family_name)):
        family_part_name = director_family_name[i]
        directorFamilyName = directorFamilyName + family_part_name 

    return directorGivenName,directorFamilyName

#function to output the credits in a table format
def credits_output(alienNameList,actorGivenList,actorFamilyList,directorGivenName,directorFamilyName):

    #first print directors name with the given and family name
    print ("Director",":",directorGivenName,directorFamilyName)

    #for loop which runs for the amount of alien names
    for i in range (len(alienNameList)):
        #print the actor and character number and their given, family and alien names
        print ("Actor",(i+1)," :",(actorGivenList[i]),(actorFamilyList[i]),"   \t Alien",(i+1),":",(alienNameList[i]))

    return''

#main function to call the other functions
def main():

    #call the extract name function with the lists of actor given and family names   
    familyhalf,givenhalf = extract_name(actorGivenList,actorFamilyList)

    #call the alien_name function with the lists of the given and family sections of the alien names
    alienNameList = alien_name(familyhalf,givenhalf)

    #call the director_name function with the sections of family names to find the director given and family name
    directorGivenName,directorFamilyName = director_name(familyhalf)    

    #call the credits_output function with the alien name list, actor given and family names, and the director given and family names, to output all the credits
    credits_output(alienNameList,actorGivenList,actorFamilyList,directorGivenName,directorFamilyName)

main()
    
    
