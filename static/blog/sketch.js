var api = 'https://newsapi.org/v2/top-headlines?country=us&category=';
  var input;
  var apikey= '&apiKey=59982f2b928e48c29577788db6fa2ef3';
const url =  "https://newsapi.org/v2/top-headlines?country=au&category=business&apiKey=59982f2b928e48c29577788db6fa2ef3";

var articles;

function setup() {
//   createCanvas(200, 200);
  background(200, 200, 200);

  noCanvas();


  var submit = select('#button');
  submit.mousePressed(topicAsk);

  input = select('#topic');

  var button = select('#button1');
  button.mousePressed(Askbus);

  var button2 = select('#button2');
  button2.mousePressed(Askhealth);



    // var url = api + 'health' + apikey;
    // loadJSON(url, gotData);



}

function topicAsk() {

    var url = api + input.value() + apikey;
    loadJSON(url, gotData);
  }

  function Askbus() {

    var url = api + 'business' + apikey;
    loadJSON(url, gotData);
    // window.location.reload(true);
  }

  function Askhealth() {
    var url = api + 'health' + apikey;
    loadJSON(url, gotData);
  }




function gotData (data) {
    articles = data.articles;

        for (i = 0; i < articles.length; i++) {
        //   document.writeln(i + 1 + ": " + articles[i]["title"]);
          // console.log(articles[i]["title"]);
          // createDiv(articles[i]["title"]);

          createElement("h1", i + 1 + ": " + articles[i]["title"]);
          createDiv(articles[i]["description"]);
          createA(
            articles[i]["url"],
            articles[i]["source"]["name"],
            articles[i]["url"]
          );

          createDiv();



        }





    }





