function (doc) {
  if(doc.tweet_longitude != "N/A" && doc.tweet_latitude != "N/A") {
    var coordinates = {longitude:doc.tweet_longitude,latitude:doc.tweet_latitude}
    emit([coordinates,doc.text],1);
  }
}