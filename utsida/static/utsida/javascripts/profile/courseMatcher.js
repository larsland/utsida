/*
 Module which handles the logic for creating course matches in /profile/courses.
 */

(function () {

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

            if (document.getElementById("courseList") != null) {
                $("#abroad_university_select").css('display', 'block');
            }
            if ($("#courseMatchList").children().length > 0) {
                $("#course_match_university_select").css('display', 'block');
                $('#create_application_btn').css('display', 'block')
            }
            else {
                $('#course_match_list_header').css('display', 'block')
            }
        },

        matchSelectedCourses: function () {

            CourseMatcher.setSelected();


            if (s.courseMatchList["homeCourseName"] && s.courseMatchList["abroadCourseName"]) {
                $.ajax({
                    data: s.courseMatchList,
                    type: "POST",
                    url: "/profile/save_course_match/",
                    success: function (response) {
                        var course_match_row = document.createElement("tr");
                        course_match_row.setAttribute("data-university", response.university);
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

                        course_match_row.appendChild(homeCourseTD);
                        course_match_row.appendChild(abroadCourseTD);

                        var content2 = course_match_row.cloneNode(true);
                        content2.setAttribute("data-id", response.course_match_id);
                        course_match_row.appendChild(deleteTD);

                        if ($("#courseMatchList").children().length == 0) {
                            var university_select = $("#course_match_university_select");

                            $("#course_match_list_header").css('display', 'none');
                            university_select.css('display', 'block');
                            university_select.attr('id', 'course_match_university_select');

                            var university_option = document.createElement("option");
                            university_option.innerText = response.university;
                            university_select.append(university_option);
                            university_select.change(courseMatchFilter());

                            $('#create_application_btn').css('display', 'block');


                        }
                        else if ($("#course_match_university_select").find('option:contains(' + response.university + ')').length == 0) {
                            var option = document.createElement("option");
                            option.innerText = response.university;
                            $("#course_match_university_select").append(option);
                            $("#course_match_university_select").val(response.university);
                        }
                        else {
                            $("#course_match_university_select").val(response.university);
                        }

                        $("#courseMatchList").append(course_match_row);
                        document.getElementById("courseMatchListModal").appendChild(content2);
                        $(document).ajaxStop(function () {
                            $(document).find('[data-toggle=confirmation]').confirmation(confirmationSettings);
                        });

                        Messager.init();
                        Messager.sendMessage("Fagene ble koblet", "success");

                        courseMatchFilter();
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
            }
            else {
                Messager.init();
                Messager.sendMessage('Du må velge et fag hjemme og borte for å koble de', 'danger')
            }


        },

        setSelected: function () {
            var awayCourse = "";
            var homeCourse = "";
            var code = "";
            var name = "";

            for (var i = 0; i < s.awayCourses.length; i++) {
                if (s.awayCourses[i].style.backgroundColor == "rgb(51, 122, 183)") {
                    awayCourse = s.awayCourses[i].innerText;

                    code = $(s.awayCourses[i]).find("#code");

                    if (code)
                        s.courseMatchList["abroadCourseCode"] = code.text();
                    else
                        s.courseMatchList["abroadCourseCode"] = "";

                    s.courseMatchList["abroadCourseName"] = $(s.awayCourses[i]).find("#name").text();
                    s.courseMatchList["abroadCourseID"] = $(s.awayCourses[i]).find("[data-id]").data("id");

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

        },

        markAwayCourse: function (block) {
            this.clearAwayCourseSelection();
            block.style.backgroundColor = "#337ab7";
            block.style.color = "white";
            s.awayCourseSelected = true;
            CourseMatcher.checkIfCanMatch();
        },

        markHomeCourse: function (block) {
            this.clearHomeCourseSelection();
            block.style.backgroundColor = "#337ab7";
            block.style.color = "white";
            s.homeCourseSelected = true;
            CourseMatcher.checkIfCanMatch();
        },

        clearAwayCourseSelection: function () {
            for (var i = 0; i < s.awayCourses.length; i++) {
                s.awayCourses[i].style.backgroundColor = "#FFF";
                s.awayCourses[i].style.color = "black";
            }
            $('#matchCourseButton').hide();
        },

        checkIfCanMatch: function () {
            s.courseMatchList["homeCourseName"] = "" ;
            s.courseMatchList["abroadCourseName"] = "";
            CourseMatcher.setSelected();
            if (s.courseMatchList["homeCourseName"] && s.courseMatchList["abroadCourseName"]) {
                $('#mark_help_text').hide();
                $('#matchCourseButton').show();
            }
            else {
                $('#mark_help_text').show();
                $('#matchCourseButton').hide();
            }
        },

        clearHomeCourseSelection: function () {
            for (var i = 0; i < s.homeCourses.length; i++) {
                s.homeCourses[i].style.backgroundColor = "#FFF";
                s.homeCourses[i].style.color = "black";
            }
            $('#matchCourseButton').hide();
        },

        toggleAddHomeCourse: function () {
            var form = document.getElementById("addHomeCourseBlock");
            var toggleBtn = document.getElementById("toggleAddHomeCourseBtn");
            form.style.display = form.style.display === 'block' ? 'none' : 'block';
            toggleBtn.innerText = toggleBtn.innerText === '-' ? '+' : '-';
        }

    };

    CourseMatcher.init();

})();