function (doc) {
  if (doc.user_location_first != null) {
    emit([doc.text, doc.lang, doc.tweet_longitude, doc.tweet_latitude, doc.retweet_count,
      doc.favorite_count, doc.user_id, doc.user_location_first, doc.user_followers_count,
      doc.user_friends_count, doc.is_retweet, doc.is_quote, doc.created_at], 1);
  }
}