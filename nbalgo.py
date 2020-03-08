color = ["RED", "RED", "RED", "YELLOW","YELLOW", "YELLOW", "YELLOW", "YELLOW", "RED", "RED"]
car_type = ["SPORTS", "SPORTS", "SPORTS", "SPORTS", "SPORTS", "SUV", "SUV", "SUV", "SUV", "SPORTS"]
origin = ["DOMESTIC", "DOMESTIC", "DOMESTIC", "DOMESTIC", "IMPORTED", "IMPORTED", "IMPORTED", "DOMESTIC", "IMPORTED", "IMPORTED"]
stolen = ["Y", "N", "Y", "N", "Y", "N", "Y", "N", "N", "Y"]

dataset = {"color":color, "car_type":car_type, "origin":origin, "stolen":stolen}
#It has colection of all columns which are in the form of list

#Calculate probablity for individual columns
def get_prob(param, data, status):
    count = 0
    for i in range (0, len(dataset[dec_param])):
        if dataset[param][i] == data and dataset[dec_param][i] == status:
            count = count + 1
    return count/dataset[dec_param].count(status)

#Calculate probablity for individual decision
def calc_prob(var):
    prob = 1
    for i in range(0, len(dataset)-1):
        
        prob = prob * get_prob(list(dataset.keys())[i], unknown[i],var)
    return prob*dataset[dec_param].count(var)/len(stolen)

def drive_away(dec_param, unknown):
    print("Probablity of",list(dict.fromkeys(dataset[dec_param]))[0],":", calc_prob(list(dict.fromkeys(dataset[dec_param]))[0]))
    print("Probablity of",list(dict.fromkeys(dataset[dec_param]))[1],":", calc_prob(list(dict.fromkeys(dataset[dec_param]))[1]))

    if calc_prob(list(dict.fromkeys(dataset[dec_param]))[0])>calc_prob(list(dict.fromkeys(dataset[dec_param]))[1]):
        print("Result: ", list(dict.fromkeys(dataset[dec_param]))[0])

    else:
        print("Result: ", list(dict.fromkeys(dataset[dec_param]))[1])

#Driver code starts here
if __name__ == "__main__":
    dec_param=input("Enter decision parameter: ")
    #This parameter is column name where decisions are stored

    unknown = []
    #List for unknown case inputs

    #Take unknown inputs
    for i in range(0, len(dataset)-1):
        unknown.append(input("Enter data for unknown "+list(dataset.keys())[i]+": "))

    #Drive away actual calculations
    drive_away(dec_param, unknown)
