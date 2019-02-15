from django.shortcuts import render
# from django.utils import simplejson
import json
# Create your views here.
# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


from firebase import firebase
firebase = firebase.FirebaseApplication('https://pwp21-56778.firebaseio.com/', None)
result_Pla = firebase.get('/images', None)
result_Bra = firebase.get('/Brands', None)
print(result_Pla)
print(result_Bra)
def get_specifics(key):
	count_individual=[]
	individual_contri=[]
	count_overall = 0
	total_contri=0
	# plas_average_contribution,wrap_average_contribution=0,0
	for i in result_Pla.values():
	  count_individual.append(i["detectionClasses"][key])
	  individual_contri.append(i["detectionScore"][key])
	  count_overall += i["detectionClasses"][key]
	  total_contri += sum(i["detectionScore"][key])
	  # count_individual_W.append([i["detectionClasses"]["Wrapper"]])
	  # W_individual_cont.append(i["detectionScore"]["Wrapper"])
	  # count_wrap += i["detectionClasses"]["Wrapper"]
	  # total_wrapper += sum(i["detectionScore"]["Wrapper"])

	# print("\nIndividual Count Plastic\n",count_individual_P)
	# print("\nIndividual Count Wrapper\n",count_individual_W)
	# print("\nIndividual score plastic\n",P_individual_cont)
	# print("\nIndividual score wrapper\n",W_individual_cont)
	# print("\nTotal Plastic Count\n",count_plas)
	# print("\nTotal Wrapper Count\n",count_wrap)
	# print("\nOverall plastic\n",total_plastic,"\nOverall wrapper\n",total_wrapper)
	avg_contri=total_contri/count_overall
	return count_individual,individual_contri,count_overall,total_contri,avg_contri
	# avg_wr=total_wrapper/count_wrap
	# print("\nAverage amount of plastic\n",avg_pl,"\nAverage amount of wrapper\n",avg_wr)
	# return count_individual_P,count_individual_P,P_individual_cont,W_individual_cont,count_plas,count_wrap,avg_pl,avg_wr
def get_specifics_brands(key):
	count_individual=[]
	individual_contri=[]
	count_overall = 0
	total_contri=0
	# plas_average_contribution,wrap_average_contribution=0,0
	for i in result_Bra.values():
	  count_individual.append(i["detectionClasses"][key])
	  individual_contri.append(i["detectionScore"][key])
	  count_overall += i["detectionClasses"][key]
	  total_contri += sum(i["detectionScore"][key])
	  # count_individual_W.append([i["detectionClasses"]["Wrapper"]])
	  # W_individual_cont.append(i["detectionScore"]["Wrapper"])
	  # count_wrap += i["detectionClasses"]["Wrapper"]
	  # total_wrapper += sum(i["detectionScore"]["Wrapper"])

	# print("\nIndividual Count Plastic\n",count_individual_P)
	# print("\nIndividual Count Wrapper\n",count_individual_W)
	# print("\nIndividual score plastic\n",P_individual_cont)
	# print("\nIndividual score wrapper\n",W_individual_cont)
	# print("\nTotal Plastic Count\n",count_plas)
	# print("\nTotal Wrapper Count\n",count_wrap)
	# print("\nOverall plastic\n",total_plastic,"\nOverall wrapper\n",total_wrapper)
	avg_contri=total_contri/count_overall
	return count_individual,individual_contri,count_overall,total_contri,avg_contri
'''i_->individual count[list of lists] || ic_->individual contribution[list of lists] || c_->Total Count{num} || 
tcntr_->total contribution{num} || acnt_->average contri'''
#<!---Plastic---!>
i_p,ic_p,c_p,tcntr_p,acntr_p = get_specifics("Plastic")
print("\n\nPLASTIC\n",i_p,ic_p,c_p,tcntr_p,acntr_p)
#<!---Wrapper---!>
i_w,ic_w,c_w,tcntr_w,acntr_w = get_specifics("Wrapper")
print("\n\nWRAPPER\n",i_w,ic_w,c_w,tcntr_w,acntr_w)
#<!---Bottle---!>
# /////i_b,ic_b,c_b,tcntr_b,acntr_b = get_specifics("Bottle")
#<!---Kurkure---!>
i_k,ic_k,c_k,tcntr_k,acntr_k = get_specifics_brands("Kurkure")
print("\n\nKURKURE\n",i_k,ic_k,c_k,tcntr_k,acntr_k)
#<!---Too-Yumm---!>
i_ty,ic_ty,c_ty,tcntr_ty,acntr_ty = get_specifics_brands("Too-Yumm")
print("\n\nTOO_YUMM\n",i_ty,ic_ty,c_ty,tcntr_ty,acntr_ty)
#<!---Bisleri---!>
i_B,ic_B,c_B,tcntr_B,acntr_B = get_specifics_brands("Bisleri")
print("\n\nBISLERI\n",i_B,ic_B,c_B,tcntr_B,acntr_B)

def modal(request):
    import os
    path = os.chdir("C://Users/Abc/Desktop/Pwp-web/Web/demo/testpwp/static/image")
    files = os.listdir(path)
    # print()
    image = ["image/"+i for i in files if i.endswith('.jpg')]
    print(image)
    context={'image':image}
    return render(request, 'testpwp/index.html',context)

def brand(request):
    import os
    path = os.chdir("C://Users/Abc/Desktop/Pwp-web/Web/demo/testpwp/static/image")
    files = os.listdir(path)
    # print()
    image = ["image/"+i for i in files if i.endswith('.jpg')]
    print(image)
    context={'image':image}
    return render(request, 'testpwp/brand.html',context)


def home(request):
	context={'1':1}
	return render(request, 'testpwp/home.html',context)


def profile(request):
	# count_individual_P,count_individual_P,P_individual_cont,W_individual_cont,count_plas,count_wrap,avg_pl,avg_wr = basic_attrs()
	average_contributions=json.dumps([acntr_p,acntr_w,acntr_k,acntr_ty,acntr_B])
	total_counts = json.dumps([c_p,c_w,c_k,c_ty,c_B])

	individual_p = json.dumps(i_p)
	individual_w = json.dumps(i_w)
	context={'average_contributions':average_contributions,'total_counts':total_counts,'individual_p':individual_p,'individual_w':individual_w}
	return render(request, 'testpwp/profiling.html',context)