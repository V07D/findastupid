var templates = '[{"id":0,"type":"input","description":"Вставьте слово, которое означало бы то же, что и слова, стоящие вне скобок.","question":"ТКАНЬ <input id=0> СОСТОЯНИЕ ВЕЩЕСТВА"},{"id":1,"type":"radio","description":"Решите анаграммы и исключите лишнее слово.","question":{"0":"КOXЙЕК", "1":"СHИHET", "2":"ОЖИВТ", "3":"ЛУФОБТ"}},{"id":2,"type":"common","description":"Найдите общее окончание для всех перечисленных слов.","question":["ДР", "М", "ТР","Ц", "Щ", "ЯГ"]},{"id":3,"type":"image_input","image":"img/question/1.jpg"}]'


// функция должна называться не parse
function parse(questions, num) {
    // красиво было бы поменять строки на генерацию объектов в доме. но нужно ли? думаю, нет
    var question = questions[num];
    switch(question.type) {
        case 'input':
            return question.question.replace(/<input id=(\d*?)>/,'(<input class="form-control question-input" id="question-input$1" style="width:100px;">)');
            
        case 'radio':
       		var result = '';
		    for(i in question.question)
			    result += '<label><input type="radio" name="question-radio" value="'+i+'"/>'+question.question[i]+'</label>';
        	return result;
        	// хорошо было бы переделать на String.join
        	
        case 'common':
            var result = '';
		    for(i in question.question)
			    result += question.question[i]+'<br>';
		    result += '<input class="form-control question-input" id="question-input0" style="width:100px;">';
		    return result;
		    // и здесь тоже хорошо было бы переделать на String.join
		    
		case 'image_input':
		    return '<img src="img/question/1.jpg"><br><input class="form-control question-input" id="question-input0" style="width:100px;">';
    }
}

/*
ДЕПРЕКАТЕД ДУЕ ТУ НИНУЖНО
function parseDescription(question, num) {
	question = JSON.parse(question)[num];
	return question.description;
}*/


$(document).ready(function(){
    var current = -1; // мда, грязный хак
    var questions = JSON.parse(templates);
    var total = questions.length;
    function changeQuestion() {
	    // current = current+1 <= total-1 ? current+1 : 0;
	    // current+1 -- следующий вопрос, total-1 -- максимальный номер вопроса
	    // переписывается в
	    //current = current + 1 < total ? current+1 : 0;
	    ++current < total || (current = 0); // потому что я могу
	    $('div#question_text').html(parse(questions, current));
	    $('p#question_description').html(questions[current].description);
	    return false; // потому что я перехуячил на кнопку, а кнопка имеет действие по дефолту
    };
    $('button#next_question').click(changeQuestion);
    changeQuestion();
});
