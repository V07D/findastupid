var questionurl = '/json/questions/';
var loggedurl = '/login/status'
var number_of_avatars = 4;

function parse(questions, num) {
    var question = questions[num];
    switch(question.type) {
        case 'input':
            return question.question.replace(/<input id=(\d*?)>/,'<input name="answer" class="form-control question-input" id="question-input$1" style="width:100px;">');
            
        case 'radio':
            var result = '';
            for(i in question.question)
                result += '<label><input type="radio" name="question-radio" value="' + i + '"/>'+question.question[i]+'</label>';
            return result;
            
        case 'common':
            var result = '';
            for(i in question.question)
                result += question.question[i] + '<br>';
            result += '<input class="form-control question-input" id="question-input0" style="width:100px;">';
            return result;
            
        case 'image_input':
            return '<img src="/static/img/question/1.jpg"><br><input class="form-control question-input" id="question-input0" style="width:100px;">';
    }
}

$(document).ready(function(){
    $.getJSON(loggedurl, function(response) {
        var logged = response.logged;
        if(!logged) {
            $('#authModal').modal();
            $('#authModalSubmit').click(function(){
                $('#authModalForm').submit();
            });
        };
    });
    
    $.getJSON(questionurl, function(response) {
        var current = -1;
        var questions = response.questions;
        var total = questions.length;
        // в рот ебал колбеки эти
        function checkAnswer() {
            var answer = $('input[name="answer"]').val();
            $.getJSON('question/check_answer', {
                id: questions[current].id,
                answer: answer
            }, function(data) {
                if (data.result) {
                    alert('ПРАВИЛЬНО');
                } else {
                    alert('РОТ ЕБАЛ');
                }
            });
        }
        function changeQuestion() {
            ++current < total || (current = 0);
            $('div#question_text').html(parse(questions, current));
            $('p#question_description').html(questions[current].description);
        };
        $('button#next_question').click(function(){
            checkAnswer();
            changeQuestion();
            return false;
        });
        changeQuestion();
    });

    var users = $('#users');
    for (var i = 0; i < number_of_avatars; ++i) {
        // делаем юзеров
        $.getJSON('/randomusers/get', function(response) {
            var user = response.data;
            users.append('<li><a href="'+user.avatar+'"><img src="'+user.avatar+'" width="30" height="30" class="img-circle">'+user.name+'</a></li>')
        })
    }
});
