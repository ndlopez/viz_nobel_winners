d3.json('github_repo/nobel_winners_cleaned.json',function(error,data){
    if(error){
	console.log(error);
    }
    d3.select('h2#data-title').text('All the nobel winners');
    d3.select('div#data pre')
	.html(JSON.stringify(data,null,4));
});
