#Class Group_3
class Group_3:
  def __init__(self, members):
    self.memberList = members
  
  #checks class schedules, determines if we can meet
  def meet_up(self, day, time): 
    #iterate over every member in our group
    #and check their class schedule
    canMeet = True
    for GroupMember in self.memberList:
      for Class in GroupMember.classSchedule:
        day_tuple = Class.day.split('/') 
        for i in range(len(day_tuple)):
          if Class.startTime <= time <= Class.endTime and (day_tuple[i] == day): 
            canMeet = False
          
    #print results
    if canMeet:
      print('We can meet on ' + day + ' at ' + str(time))
    else:
      print("We can't meet on " + day + " at " + str(time))   

   

  def print_members(self):
    print(self.memberList)
    
  # === Class GroupMember ===
class GroupMember:
  def __init__(self, name, major, classSchedule):
    self.name = name
    self.major = major
    self.classSchedule = classSchedule
  
  def print_schedule(self):
    print(self.name + "'s Schedule:")
    i = 0
    for i in range(len(self.classSchedule)):
      self.classSchedule[i].print_class_info()
    print('')
      
      
  #Class Class
class Class:
  def __init__(self, dep, cN, dy, sT, eT):
    self.department = dep
    self.classNumber = cN
    self.day = dy
    self.startTime = sT
    self.endTime = eT

  def print_class_info(self):
    print(self.department + " " + str(self.classNumber) + ": " + self.day + " " + str(self.startTime) + " to " + str(self.endTime)) 
    

#main
#classes
seniorSeminar = Class('CS', 4630, 'M', 13, 13.50)
cryptology = Class('CS', 4600, 'M/W', 14.30, 15.45)
programmingLanguages = Class('CS', 4080, 'T/Th', 10.0, 11.15)
operatingSystems = Class('CS', 4310, 'T/Th', 13.0, 14.15)
operatingSystemsMWF = Class('CS', 4310, 'M/W/F', 10, 10.5)
computersAndSociety = Class('CS', 3750, 'T/Th', 10, 11.15)
numMethods = Class('CS', 3010, 'T/Th', 14.30, 15.45)
algorithms = Class('CS', 3310, 'M/W', 11, 12.50)
dataStructures = Class('CS', 2400, 'M/W', 17, 18.5)
linearAlg = Class('MAT', 2250, 'T/Th', 10, 11.5)
polySci = Class('PLS', 2010, 'T/Th', 8.3, 9.45)
physics = Class('PHY', 1510, 'T/Th', 13, 14.15)
physicsLab = Class('PHYL', 1510, 'W', 8, 11)
statistics = Class('STA', 2260, 'M/W', 13, 14.15)
history = Class('HST', 3370, 'T/Th', 13, 14.15)
drugsAndSociety = Class('AVS', 2211, 'T', 14, 15.15)


#our schedules
jakesSchedule = [seniorSeminar, cryptology, programmingLanguages, operatingSystems]
chrisSchedule = [programmingLanguages, seniorSeminar, numMethods, algorithms, cryptology]
zackSchedule = [linearAlg, polySci, physics, physicsLab, statistics, dataStructures]
colbysSchedule = [operatingSystemsMWF, history, computersAndSociety, drugsAndSociety]
#instantiating ourselves to the group
Jake = GroupMember('Jake', 'CS', jakesSchedule)
Chris = GroupMember('Chris','CS', chrisSchedule)
Zack = GroupMember('Zack','CS', zackSchedule)
Colby = GroupMember('Colby', 'CS', colbysSchedule)


#now test...
mems = [Jake, Chris, Zack, Colby]

for GroupMember in mems:
  GroupMember.print_schedule()

ourGroup = Group_3(mems)

ourGroup.meet_up('M', 12.00)

ourGroup.meet_up('W', 17.30) 

ourGroup.meet_up('Th', 12.00) # <== U-hour

ourGroup.meet_up('F', 9.59)

ourGroup.meet_up('F', 10.00)

