/*
 Module which handles the logic for creating course matches in /profile/courses.
 */

(function(){

    var s;

    CourseMatcher = {

        s: {
            awayCourses: null,
            homeCourses: null,
            awayCourseSelected: false,
            homeCourseSelected: false,
            courseMatchesContainer: null,
            superVisorEmail: null,
            wrapper: null
        },

        init: function () {
            s = this.s;
            if (document.getElementById("courseList")) {
                s.awayCourses = document.getElementById("courseList").children;
            }
            else {
                s.awayCourses = [];
            }
            s.homeCourses = document.getElementById("homeCourseList").children;
            s.courseMatchesContainer = document.getElementById("courseMatches");
            s.wrapper = document.getElementById("courseMatchesWrapper");
            s.courseMatchList = {};
        }
        ,

        matchSelectedCourses: function () {
            var awayCourse = "";
            var homeCourse = "";
            var code = "";
            var name = "";

            for (var i = 0; i < s.awayCourses.length; i++) {
                if (s.awayCourses[i].style.backgroundColor == "rgb(51, 122, 183)") {
                    awayCourse = s.awayCourses[i].innerText;
                    if (/-/.test(awayCourse)) {
                        code = s.awayCourses[i].children[0].innerText;
                        name = s.awayCourses[i].children[1].innerText;
                        s.courseMatchList["abroadCourseCode"] = code;
                        s.courseMatchList["abroadCourseName"] = name;
                    }
                    else {
                        code = "";
                        name = s.awayCourses[i].children[0].innerText;
                        s.courseMatchList["abroadCourseName"] = name;
                        s.courseMatchList["abroadCourseCode"] = code
                    }
                }
            }

            for (var j = 0; j < s.homeCourses.length; j++) {
                if (s.homeCourses[j].style.backgroundColor == "rgb(51, 122, 183)") {
                    homeCourse = s.homeCourses[j].innerText;
                    code = s.homeCourses[j].children[0].innerText;
                    name = s.homeCourses[j].children[1].innerText;
                    s.courseMatchList["homeCourseCode"] = code;
                    s.courseMatchList["homeCourseName"] = name;
                }
            }
            $.ajax({
                data: s.courseMatchList,
                type: "POST",
                url: "/profile/save_course_match/",
                success: function (response) {
                    var content = document.createElement("tr");
                    var abroadCourseTD = document.createElement("td");

                    if (s.courseMatchList["abroadCourseCode"] == "")
                        abroadCourseTD.innerText = s.courseMatchList["abroadCourseName"];

                    abroadCourseTD.innerText = s.courseMatchList["abroadCourseCode"] + "  " + s.courseMatchList["abroadCourseName"];

                    var homeCourseTD = document.createElement("td");
                    homeCourseTD.innerText = s.courseMatchList["homeCourseCode"] + "  " + s.courseMatchList["homeCourseName"];

                    var deleteTD = document.createElement('td');
                    var deleteBtn = document.createElement('span');
                    deleteBtn.className = "glyphicon glyphicon-remove pointer";
                    deleteBtn.setAttribute("data-toggle", "confirmation");
                    deleteBtn.setAttribute("data-type", "course_match");
                    deleteBtn.setAttribute("data-id", response.course_match_id);
                    deleteTD.appendChild(deleteBtn);

                    content.appendChild(abroadCourseTD);
                    content.appendChild(homeCourseTD);
                    content.appendChild(deleteTD);

                    var content2 = content.cloneNode(true);
                    document.getElementById("courseMatchList").appendChild(content);
                    document.getElementById("courseMatchListModal").appendChild(content2);

                    refreshConfirmation();

                    Messager.init();
                    Messager.sendMessage("Fagene ble koblet", "success");
                },
                error: function (error) {
                    if (error.status == 409) {
                        Messager.init();
                        Messager.sendMessage("Koblingen er allerede i din profil!", "danger");
                    }
                    else if (error.status == 406) {
                        Messager.init();
                        Messager.sendMessage("Det finnes fag fra et annet universitet i din profil", "danger");
                    }
                }
            });


        },

        markAwayCourse: function (block) {
            this.clearAwayCourseSelection();
            block.style.backgroundColor = "#337ab7";
            block.style.color = "white";
            s.awayCourseSelected = true;
        },

        markHomeCourse: function (block) {
            this.clearHomeCourseSelection();
            block.style.backgroundColor = "#337ab7";
            block.style.color = "white";
            s.homeCourseSelected = true;
        },

        clearAwayCourseSelection: function () {
            for (var i = 0; i < s.awayCourses.length; i++) {
                s.awayCourses[i].style.backgroundColor = "#FFF";
                s.awayCourses[i].style.color = "black";
            }
        },

        clearHomeCourseSelection: function () {
            for (var i = 0; i < s.homeCourses.length; i++) {
                s.homeCourses[i].style.backgroundColor = "#FFF";
                s.homeCourses[i].style.color = "black";
            }
        },

        toggleAddHomeCourse: function() {
            var form = document.getElementById("addHomeCourseBlock");
            var toggleBtn = document.getElementById("toggleAddHomeCourseBtn");
            form.style.display = form.style.display === 'block' ? 'none' : 'block';
            toggleBtn.innerText = toggleBtn.innerText === '-' ? '+' : '-';

        }

    };

    CourseMatcher.init();

})();