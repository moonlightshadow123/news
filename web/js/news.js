var jsonData;
var news_url = "http://127.0.0.1:8000/news";//"../../json/news.json";
var $form = $("#form");
var $newsContainer = $("#newsContainer");
var $newsListContainer = $("#newsListContainer");
var $sect_template = $("#sect_template").clone().attr("id", "");
var simpleBar;
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
	console.log("getData!");
	$.getJSON(url, function(data){
		jsonData = data;
		genSect(data["articles"]);
		$("button.url").click(function(){
			openUrl($(this).attr("data-url"));
		});
	});
}

function genSect(data){
	var container;
	if(!simpleBar){
		container = $newsListContainer;
	}else{
		container = $newsListContainer.find("simplebar-content");
	}
	container.children().remove();
	data.forEach(function(article, idx){
		var title = article["title"];
		var description = article["description"];
		var urlToImg = article["urlToImage"];
		var content = article["content"];
		var date = article["publishedAt"];
		var url = article["url"];
		var $sect = $sect_template.clone();
		$sect.find('img').attr("src", urlToImg)
		$sect.find("h2").text(title);
		$sect.find('span.date').append( date);
		$sect.find("span.description").text(description);
		if(content)
			$sect.find("p.content").text(content);
		else
			$sect.find("p.content").remove();
		$sect.find("button.url").attr("data-url", url);
		container.append($sect);
	//return $sect;
	});
	$newsListContainer.height(window.innerHeight-100);
	if(!simpleBar){
		simpleBar = new SimpleBar($newsListContainer[0]);
		simpleBar.recalculate();
	}
}

function submitform(e){
	console.log("submit!");
	var category = $form.find('input[name="category"]').val();
	var keyword = $form.find('input[name="keyword"]').val();
	var url = news_url + "?keyword=" + keyword + "&category=" + category;
	getData(news_url);
	return false;
}

$(function(){
	$form.on("submit", submitform);
	getData(news_url);
});