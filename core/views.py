from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request, r'C:\Users\skdan\Documents\2022_Fall\웹프실\final_project\eft_market\core\templates\core\mainpage.html')