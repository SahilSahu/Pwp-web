from django.shortcuts import render
# from django.utils import simplejson
import json
# Create your views here.
# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


detection_classes = [[1,3,3,1,1,1,1,1,2,3,2,1,1],[2,3,1,1,1,3,3,1,1,1,1,1,8,1,10],[1,1,1,2,3,3,1,2,3,3,1,1,8,8,3,2,1,1,1,3,8,2,1,2,2,8,3,1,8,8,2,1,8,1,8,2,9,8]]

detection_score = [[9.0574878e-01, 7.0590609e-01, 1.4935657e-01, 1.4761624e-01, 2.4734005e-02,
 2.1228779e-02, 1.4216424e-02, 8.2495036e-03, 7.5826286e-03, 7.0797699e-03
, 5.5995388e-03],[9.9744785e-01, 8.9541668e-01, 8.2370239e-01, 4.6380636e-01, 1.1927086e-02,
 8.3097331e-03],[9.0047395e-01, 8.9557219e-01, 8.1574726e-01, 6.4440078e-01, 5.2770746e-01,
 3.8250548e-01]]
# percentage=[]
gt_40 = []
dom_class = []
dom_class_name = []
for i in range(len(detection_score)):
  for j in range(len(detection_score[i])):
    detection_score[i][j] = (float(detection_score[i][j])*100)

  gt_40.append(detection_score[i])
    
# print(gt_40)
# print("Before Condition",gt_40)
for i in range(len(gt_40)):
  gt_40[i]=[j for j in gt_40[i] if j>40]

for i in range(len(detection_classes)):
  dom_class.append(detection_classes[i][0:len(gt_40[i])])
  # print(len(gt_40[i]))
print(dom_class)
print(gt_40)
for i in range(len(dom_class)):
  for j in range(len(dom_class[i])):
    if dom_class[i][j] == 1:
      dom_class[i][j] = "Plastic"
    if dom_class[i][j] == 2:
      dom_class[i][j] = "kurkure"
    if dom_class[i][j] == 3:
      dom_class[i][j] = "wrapper"
    if dom_class[i][j] == 4:
      dom_class[i][j] = "bottle"
    if dom_class[i][j] == 5:
      dom_class[i][j] = "pepsi"
    if dom_class[i][j] == 6:
      dom_class[i][j] = "Bisleri"
    if dom_class[i][j] == 7:
      dom_class[i][j] = "Bailey"
    if dom_class[i][j] == 8:
      dom_class[i][j] = "Coca-Cola"
    if dom_class[i][j] == 9:
      dom_class[i][j] = "cardboard"
    if dom_class[i][j] == 10:
      dom_class[i][j] = "plastic-bottle"
    if dom_class[i][j] == 11:
      dom_class[i][j] = "kinley"
    if dom_class[i][j] == 0:
      dom_class[i][j] = "Something else"

print(dom_class)
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    context={'1':2}
    count_individual = []
    # count_p,count_w,count_k,count_b,count_ps,count_Bis,count_Bl,count_C,count_c,count_plb,count_Kin = 0,0,0,0,0,0,0,0,0,0,0
    for i in range(len(dom_class)):
      count_p = dom_class[i].count('Plastic')
      count_k = dom_class[i].count('kurkure')
      count_w = dom_class[i].count('wrapper')
      count_b = dom_class[i].count('bottle')
      count_ps = dom_class[i].count('pepsi')
      count_Bis = dom_class[i].count('Bisleri')
      count_Bl = dom_class[i].count('Bailey')
      count_C = dom_class[i].count('Coca-Cola')
      count_c = dom_class[i].count('cardboad')
      count_plb = dom_class[i].count('plastic-bottle')
      count_Kin = dom_class[i].count('kinley')
      count_individual.append([count_p,count_w,count_k,count_b,count_ps,count_Bis,count_Bl,count_C,count_c,count_plb,count_Kin])
    print(count_individual)

    return render(request, 'testpwp/modal.html',context)

def home(request):
	context={'1':1}
	return render(request, 'testpwp/home.html',context)


def profile(request):
	
	# detection_classes = [[1,3,3,1,1,1,1,1,2,3,2,1,1],[2,3,1,1,1,3,3,1,1,1,1,1,8,1,10],[1,1,1,2,3,3,1,2,3,3,1,1,8,8,3,2,1,1,1,3,8,2,1,2,2,8,3,1,8,8,2,1,8,1,8,2,9,8]]

	# detection_score = [[9.0574878e-01, 7.0590609e-01, 1.4935657e-01, 1.4761624e-01, 2.4734005e-02,
	#  2.1228779e-02, 1.4216424e-02, 8.2495036e-03, 7.5826286e-03, 7.0797699e-03
	# , 5.5995388e-03],[9.9744785e-01, 8.9541668e-01, 8.2370239e-01, 4.6380636e-01, 1.1927086e-02,
	#  8.3097331e-03],[9.0047395e-01, 8.9557219e-01, 8.1574726e-01, 6.4440078e-01, 5.2770746e-01,
	#  3.8250548e-01]]
	# # percentage=[]
	# gt_40 = []
	# dom_class = []
	# dom_class_name = []
	# for i in range(len(detection_score)):
	#   for j in range(len(detection_score[i])):
	#     detection_score[i][j] = (float(detection_score[i][j])*100)

	#   gt_40.append(detection_score[i])
	    
	# # print(gt_40)
	# # print("Before Condition",gt_40)
	# for i in range(len(gt_40)):
	#   gt_40[i]=[j for j in gt_40[i] if j>40]

	# for i in range(len(detection_classes)):
	#   dom_class.append(detection_classes[i][0:len(gt_40[i])])
	#   # print(len(gt_40[i]))
	# print(dom_class)
	# print(gt_40)
	# for i in range(len(dom_class)):
	#   for j in range(len(dom_class[i])):
	#     if dom_class[i][j] == 1:
	#       dom_class[i][j] = "Plastic"
	#     if dom_class[i][j] == 2:
	#       dom_class[i][j] = "kurkure"
	#     if dom_class[i][j] == 3:
	#       dom_class[i][j] = "wrapper"
	#     if dom_class[i][j] == 4:
	#       dom_class[i][j] = "bottle"
	#     if dom_class[i][j] == 5:
	#       dom_class[i][j] = "pepsi"
	#     if dom_class[i][j] == 6:
	#       dom_class[i][j] = "Bisleri"
	#     if dom_class[i][j] == 7:
	#       dom_class[i][j] = "Bailey"
	#     if dom_class[i][j] == 8:
	#       dom_class[i][j] = "Coca-Cola"
	#     if dom_class[i][j] == 9:
	#       dom_class[i][j] = "cardboard"
	#     if dom_class[i][j] == 10:
	#       dom_class[i][j] = "plastic-bottle"
	#     if dom_class[i][j] == 11:
	#       dom_class[i][j] = "kinley"
	#     if dom_class[i][j] == 0:
	#       dom_class[i][j] = "Something else"

	# print(dom_class)
	count_p,count_w,count_k,count_b,count_ps,count_Bis,count_Bl,count_C,count_c,count_plb,count_Kin = 0,0,0,0,0,0,0,0,0,0,0
	for i in range(len(dom_class)):
	  count_p += dom_class[i].count('Plastic')
	  count_k += dom_class[i].count('kurkure')
	  count_w += dom_class[i].count('wrapper')
	  count_b += dom_class[i].count('bottle')
	  count_ps += dom_class[i].count('pepsi')
	  count_Bis += dom_class[i].count('Bisleri')
	  count_Bl += dom_class[i].count('Bailey')
	  count_C += dom_class[i].count('Coca-Cola')
	  count_c += dom_class[i].count('cardboad')
	  count_plb += dom_class[i].count('plastic-bottle')
	  count_Kin += dom_class[i].count('kinley')

	print("\n\nFollowing is the analysis =>\n\nPlastic->",count_p,"\nkurkure->",count_k,"\nwrapper->",count_w,"\nbottle->",count_b,"\npepsi->",count_ps,"\nBisleri->",count_Bis,
	"\nBailey->",count_Bl,"\nCoca-Cola->",count_C,"\ncardboard->",count_c,"\nplastic-bottle->",count_plb,"\nkinley->",count_Kin)
	total_count=count_p+count_k+count_w+count_b+count_ps+count_Bis+count_Bl+count_C+count_c+count_plb+count_Kin
	count=json.dumps([count_p,count_k,count_w,count_b,count_ps,count_Bis,count_Bl,count_C,count_c,count_plb,count_Kin])
	count_per=json.dumps([(count_p*100/total_count),count_k*100/total_count,count_w*100/total_count,count_b*100/total_count,count_ps*100/total_count,count_Bis*100/total_count,count_Bl*100/total_count,count_C*100/total_count,count_c*100/total_count,count_plb*100/total_count,count_Kin*100/total_count])
	context={'count':count,'count_per':count_per}
	return render(request, 'testpwp/profiling.html',context)