var data;
var $weiboContainer = $("#weiboContainer");
function getData(url, func=null){
	$.getJSON(url, function(jsonData){
		data = jsonData;
		if(func!=null)func(data);
	});
}

function genDiv(data){
	data.forEach(function(ele, idx){
		var title = ele["title"];
		var num = ele["num"];
		var url = ele["url"];
		var score = ele["score"];
		var $snum = $('<div class="col-1">').append($('<span>').text(num));
		var $a = $('<div class="col-8">').append($('<a target="_blank">').text(title).attr("href", url));
		var $sspan = $('<div class="col-3">').append($('<span clas="col-3" >').text(score));
		var $div = $('<div class="shadow">').append($snum, $a, $sspan);
		$weiboContainer.append($div) ;
	});
	$weiboContainer.height(window.innerHeight/2);
	const simpleBar = new SimpleBar(document.getElementById('weiboContainer'));
	simpleBar.recalculate();
}

$(function(){
	getData("weibo.json", genDiv);
	//$weiboContainer.height(window.innerHeight/2);
});