var html_url = "../html/template.html";
class Toplist{
	json_url;
	data;
	color;
	$container;
	$listContainer;
	$logoimg;
	$datespan
	$updatebtn;
	constructor(json_url, $container){
		this.json_url = json_url;
		this.$container = $container;
		this.$container.load(html_url, function(){
						console.log(this.$container.find(".logoimg"));
						this.getHtml();
		}.bind(this));
	}

getHtml(){
	//this.$container.load(html_url, function(){
		console.log(this);
		this.$listContainer = this.$container.find(".listContainer");
		this.$logoimg = this.$container.find(".logoimg");
		this.$datespan = this.$container.find(".datespan");
		this.$updatebtn = this.$container.find(".updatebtn");
		this.$updatebtn.click(this.getData.bind(this));
		this.getData();
	//});
}

getData(){
	console.log("getData!");
	$.getJSON(this.json_url, function(jsonData){
		console.log(jsonData);
		this.data = jsonData;
		this.$logoimg.attr("src", this.data["logo"]);
		this.$datespan.text("updated at: "+this.data["date"]);
		this.color = this.data["color"];
		this.genDiv( this.data["list"]);
	}.bind(this));
}

genDiv(data){
	var container;
	if(this.simpleBar) container=$(this.simpleBar.contentEl);
	else container=this.$listContainer;
	container.children().remove();
	//this.$listContainer = this.$container.find(".listContainer");
	data.forEach(function(ele, idx){
		var title = ele["title"];
		var num = ele["num"];
		var url = ele["url"];
		var score = ele["score"];
		var $snum = $('<div class="col-1">').append($('<span style="font-weight:700">').text(num));
		var $a = $('<div class="col-8">').append($('<a target="_blank">').text(title).attr("href", url));
		var $sspan = $('<div class="col-3">').append($('<span clas="col-3" >').text(score));
		var $div = $('<div class="shadow grid">').append($snum, $a, $sspan);
		container.append($div);
	}.bind(this));
	// Height and Simple bar
	this.$listContainer.height(window.innerHeight/2);
	if(!this.simpleBar){
		this.simpleBar = new SimpleBar(this.$listContainer[0]);
		this.simpleBar.recalculate();
	}
	var color = this.color;
	console.log(color);
	container.find(".shadow").mouseover( function(){
		$(this).css("font-weight", "700").css("background-color", color);
	});
	container.find(".shadow").mouseleave( function(){
		$(this).css("font-weight", "").css("background-color", "");;
	});
}
}

$(function(){
	var bili = new Toplist("../../json/bili.json", $("#biliContainer"));
	var zhihu = new Toplist("../../json/zhihu.json", $("#zhihuContainer"));
	//getData("../../json/bili.json", genDiv);
	//$weiboContainer.height(window.innerHeight/2);
});