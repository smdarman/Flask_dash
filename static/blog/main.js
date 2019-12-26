//const wordnikAPI =
//  "https://newsapi.org/v2/top-headlines?country=au&category=health&apiKey=59982f2b928e48c29577788db6fa2ef3";
//
//
//
//
// async function catchNews() {
//   const response = await fetch(wordnikAPI);
//   const data = await response.json();
//    articles = data.articles;
//    appendData(articles);
//    };
//    catchNews();
//
////fetch(wordnikAPI)
////  .then(response => response.json())
////  .then(data => {
////    articles = data.articles;
////    appendData(articles);
////    //articles = articles['title']
////
////    // for (const val of Object.values(articles)) {
////    //   for (i = 0; i < articles.length; i++) {
////    //     // document.writeln(i + 1 + ": " + articles[i]["title"]);
////    //     console.log(articles[2]["title"]);
////    //   }
////    // }
////    // return fetch(articles[2]["title"]);
////  })
////  .catch(error => console.error(error));
//
//// .catch(error => console.error(error));
//
//
//function appendData(articles) {
//  for (i = 0; i < articles.length; i++) {
//    // document.writeln(i + 1 + ": " + articles[i]["title"]);
//    // console.log(articles[2]["title"]);
//    // *ngIf="${news}"
//    // var div = document.createElement("h1");
//
//    template = news => {
//      return `
//  <div class="item">
//    <h1>${news.title}</h1>
//    <a href="${news.url}" target="_blank">${news.source.name}</a>
//    <h4>${news.description}</h4>
//    <img  src="${news.urlToImage}"  height="322" width="522" onerror="this.onerror=null;this.src='https://placeimg.com/200/300/animals';">
//    </div>
//
//    `;
//    };
//
//    document.getElementById("app").innerHTML = `
//    <h1> Number of news ${articles.length} </h1>
//${articles.map(template).join("")}
//      <p> ${i + 1 + ": " + articles[i].title} </p>
//      <div> ${articles[i].url} </div>
//      <P> ${2 + 2} <p>
//
//    `;
//  }
//}
