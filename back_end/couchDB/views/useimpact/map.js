function (doc) {
  emit([doc.id, doc._id],
    {followers: doc.user_followers_count,
      textlength: doc.text.split(" ").length});
}
