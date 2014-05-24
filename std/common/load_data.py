import csv,os





def load(path):

    with open(path) as foo:

        reader = csv.reader(foo)

        for row in reader:

            for each in row:
                print each,
            print "................"
        
            
