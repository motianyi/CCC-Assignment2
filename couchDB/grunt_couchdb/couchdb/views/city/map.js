function (doc) {
    if(doc.user_location_first != null) {
      emit([doc.user_location_first], 1);
    }
  }