from django.shortcuts import render
import requests
import json
from .forms import *
from profiles.models import *


def index(request):
    return render(request, "utsida/index.html")


def process(request):
    form = QueryCaseBaseForm()
    return render(request, "utsida/process.html", {"form": form})


def result(request):
    if request.method == 'POST':
        form = QueryCaseBaseForm(request.POST)
        user_profile = User.objects.get(username=request.user).profile
        institute = user_profile.institute.__str__()
        courses_taken = []
        courses_taken_object = request.user.profile.coursesToTake.all()

        for course in courses_taken_object:
            courses_taken.append(str(course))

        if form.is_valid():
            payload = json.dumps({
                "Institute": institute,
                "Continent": form.data["continent"],
                "Country": form.data["country"],
                "University": form.data["university"],
                "Language": form.data["language"],
                "StudyPeriod": form.data["studyPeriod"],
                "AcademicQuality": form.data["academicQualityRating"],
                "SocialQuality": form.data["socialQualityRating"],
            })
            headers = {
                'content-type': 'application/json'
            }

            r = requests.post("http://localhost:8080/retrieval?casebase=main_case_base&concept%20name=Trip",
                              data=payload,
                              headers=headers
                              ).json()["similarCases"]

            full_similar_cases = []

            for key, value in r.items():
                full_case = requests.get("http://localhost:8080/case?caseID=" + key).json()["case"]
                full_case["Subjects"] = full_case["Subjects"].split('!')
                full_case["Similarity"] = "%.3f" % value
                full_similar_cases.append(full_case)

            sorted_full_similar_cases = sorted(full_similar_cases, key=lambda k: k['Similarity'], reverse=True)

            courses = request.user.profile.coursesToTake.all()

            course_wanted_to_be_taken_matches = {}

            for course in courses:
                results = CourseMatch.objects.filter(homeCourse=course)
                if results:
                    print(results)
                    for result in results:
                        course_wanted_to_be_taken_matches[str(result.abroadCourse)] = course.code

            print(course_wanted_to_be_taken_matches)

            return render(request, 'utsida/result.html',
                          {'form': form, 'similar_cases': sorted_full_similar_cases, 'courses_taken': courses_taken, 'matches': course_wanted_to_be_taken_matches})
    else:
        form = QueryCaseBaseForm()

    return render(request, 'utsida/process.html', {'form': form})


def courseMatch(request):
    course_matches = CourseMatch.objects.all()
    university_list = University.objects.all()
    context = {"course_match_list": course_matches, "university_list": university_list}
    return render(request, "utsida/courseMatch.html", context)
