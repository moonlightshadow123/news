var data;
var $container = $("#container");
var $newsContainer = $("#newsContainer");
var $sect_template = $("#sect_template");
//$("select").selectmenu().selectmenu( "menuWidget" ).addClass("active");

function openUrl(url){
	var win = window.open(url, '_blank');
	if (win) {
	    //Browser has allowed it to be opened
	    win.focus();
	} else {
	    //Browser has blocked it
	    alert('Please allow popups for this website');
	}
}

function getData(url){
	$.getJSON(url, function(jsonData){
		data = jsonData["articles"];
		data.forEach(function(article, idx){
			var $sect = genSect(article);
			$container.append($sect);
		});
		$sect_template.remove();
		$sect_template.height(window.innerHeight/2);
		const simpleBar = new SimpleBar(document.getElementById('sect_template'));
		simpleBar.recalculate();
		$("button.url").click(function(){
			openUrl($(this).attr("data-url"));
		});
	});
}

function genSect(data){
	var title = data["title"];
	var description = data["description"];
	var urlToImg = data["urlToImage"];
	var content = data["content"];
	var url = data["url"];
	$sect = $sect_template.clone();
	$sect.find('img').attr("src", urlToImg)
	$sect.find("h2").text(title);
	$sect.find("p.description").text(description);
	$sect.find("p.content").text(content);
	$sect.find("button.url").attr("data-url", url);
	return $sect;
}

$(function(){
	getData('../../json/news.json');
});