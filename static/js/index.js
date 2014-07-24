var templates = '[{"id":0,"type":"input","description":"Вставьте слово, которое означало бы то же, что и слова, стоящие вне скобок.","question":"ТКАНЬ <input id=0> СОСТОЯНИЕ ВЕЩЕСТВА"},{"id":1,"type":"radio","description":"Решите анаграммы и исключите лишнее слово.","question":{"0":"КOXЙЕК", "1":"СHИHET", "2":"ОЖИВТ", "3":"ЛУФОБТ"}},{"id":2,"type":"common","description":"Найдите общее окончание для всех перечисленных слов.","question":["ДР", "М", "ТР","Ц", "Щ", "ЯГ"]},{"id":3,"type":"image_input","image":"img/question/1.jpg"}]'



parse = function(question,num) {
		question = JSON.parse(question)[num];
		if(question.type == "input") {
			return question.question.replace(/<input id=(\d*?)>/,'(<input class="form-control question-input" id="question-input$1" style="width:100px;">)')
		}
		else if(question.type == 'radio') {
			var result = '';
			for(i in question.question) {
				result += '<label><input type="radio" name="question-radio" value="'+i+'"/>'+question.question[i]+'</label>';
			}
			return result;
		}
		else if(question.type == 'common') {
			var result = '';
			for(i in question.question) {
				result += question.question[i]+'<br>';
			}
			result += '<input class="form-control question-input" id="question-input0" style="width:100px;">';
			return result;
		}
		else if(question.type == 'image_input') {
			return '<img src="static/img/question/1.jpg"><br><input class="form-control question-input" id="question-input0" style="width:100px;">';
		}
	}
parseDescription = function(question,num) {
	question = JSON.parse(question)[num];
	return question.description;
}

var current = 0;
var total = JSON.parse(templates).length;
$('#next_question').click(function() {
	current = current+1 <= total-1 ? current+1 : 0;
	$('#question_text').html(parse(templates,current));
	$('#question_description').html(parseDescription(templates,current));
});
