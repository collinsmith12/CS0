hw = [100,100,100,85,65,100,100,100,0,105,105]
hwgrade = .2
hwaverage= float(sum(hw)/11*hwgrade)
print "average homework score" + str(hwaverage)

quiz = [93,87,100,100,100,72]
quizgrade = .25
quizaverage= float(sum(quiz)/6*quizgrade)
print "average quiz score" + str(quizaverage)

test = [98,92,75,80]
testgrade = .3
testaverage= float(sum(test)/4*testgrade)
print "average test score" + str(testaverage)

midterm = (85)
midtermgrade = .10
midtermaverage= float((midterm)*midtermgrade)
print "average midterm score" + str(midtermaverage)
 
percentagelist = [testaverage, hwaverage, quizaverage, midtermaverage]
overallpercentage= sum(percentagelist)
print"average grade without final exam=" + str(overallpercentage)

passinggrade= 90
scoreneededforfinal= passinggrade- (overallpercentage)
scoreneededforfinalexam= scoreneededforfinal / .15
print "the score you need on final to pass it"+ str(scoreneededforfinalexam)

