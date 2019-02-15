from django.shortcuts import render
# from django.utils import simplejson
import json
# Create your views here.
# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


from firebase import firebase
firebase = firebase.FirebaseApplication('https://pwp21-56778.firebaseio.com/', None)
result = firebase.get('/images', None)
print(result)
def basic_attrs():
	count_individual_P,count_individual_W=[],[]
	P_individual_cont,W_individual_cont=[],[]
	count_plas,count_wrap=0,0
	total_plastic,total_wrapper=0,0
	# plas_average_contribution,wrap_average_contribution=0,0
	for i in result.values():
	  # print(i)
	  # detection_classes.update(i["detectionClasses"]);
	  # detection_scores.update(i["detectionScore"]);
	  # print(i["detectionClasses"]["Plastic"])
	  count_individual_P.append([i["detectionClasses"]["Plastic"]])
	  P_individual_cont.append(i["detectionScore"]["Plastic"])
	  count_plas += i["detectionClasses"]["Plastic"]
	  total_plastic += sum(i["detectionScore"]["Plastic"])
	  count_individual_W.append([i["detectionClasses"]["Wrapper"]])
	  W_individual_cont.append(i["detectionScore"]["Wrapper"])
	  count_wrap += i["detectionClasses"]["Wrapper"]
	  total_wrapper += sum(i["detectionScore"]["Wrapper"])

	print("\nIndividual Count Plastic\n",count_individual_P)
	print("\nIndividual Count Wrapper\n",count_individual_W)
	print("\nIndividual score plastic\n",P_individual_cont)
	print("\nIndividual score wrapper\n",W_individual_cont)
	print("\nTotal Plastic Count\n",count_plas)
	print("\nTotal Wrapper Count\n",count_wrap)
	print("\nOverall plastic\n",total_plastic,"\nOverall wrapper\n",total_wrapper)
	avg_pl=total_plastic/count_plas
	avg_wr=total_wrapper/count_wrap
	print("\nAverage amount of plastic\n",avg_pl,"\nAverage amount of wrapper\n",avg_wr)
	return count_individual_P,count_individual_P,P_individual_cont,W_individual_cont,count_plas,count_wrap,avg_pl,avg_wr
def modal(request):
    import os
    path = os.chdir("C://Users/Pc/Desktop/Pwp-web/Web/demo/testpwp/static/image")
    files = os.listdir(path)
    # print()
    image = ["image/"+i for i in files if i.endswith('.jpg')]
    print(image)
    context={'image':image}
    return render(request, 'testpwp/modal.html',context)

def brand(request):
    import os
    path = os.chdir("C://Users/Pc/Desktop/Pwp-web/Web/demo/testpwp/static/image")
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
	count_individual_P,count_individual_P,P_individual_cont,W_individual_cont,count_plas,count_wrap,avg_pl,avg_wr = basic_attrs()
	return render(request, 'testpwp/profiling.html',context)